import machine
import time
from machine import Pin, PWM, ADC
import network
import socket

# ESP32-C3 RF Control Configuration
class RFController:
    def __init__(self):
        # GPIO pins for RF module
        self.tx_pin = Pin(3, Pin.OUT)  # Transmit pin
        self.rx_pin = Pin(4, Pin.IN)   # Receive pin
        self.data_pin = Pin(5, Pin.OUT)  # Data pin
        self.freq_pin = Pin(6, Pin.OUT)  # Frequency control
        
        # PWM for frequency modulation
        self.pwm = PWM(self.freq_pin)
        self.pwm.freq(1000)
        
        # ADC for signal sensing
        self.adc = ADC(Pin(0))  # ADC pin for signal level
        self.adc.atten(ADC.ATTN_11DB)
        
        self.is_transmitting = False
        self.current_frequency = 433  # MHz (common ISM band)
        self.power_level = 100
        
    def set_frequency(self, freq_mhz):
        """Set RF frequency (433, 868, 2400 MHz bands)"""
        self.current_frequency = freq_mhz
        # Map frequency to PWM duty cycle (0-1023)
        freq_map = {433: 256, 868: 512, 2400: 768}
        duty = freq_map.get(freq_mhz, 256)
        self.pwm.duty(duty)
        print(f"Frequency set to {freq_mhz} MHz")
        
    def set_power(self, level):
        """Set transmission power level (0-100)"""
        self.power_level = max(0, min(100, level))
        self.pwm.duty(int(self.power_level * 10.23))
        print(f"Power level set to {self.power_level}%")
        
    def transmit(self, data, duration=1):
        """Transmit RF signal with data"""
        self.is_transmitting = True
        self.tx_pin.on()
        
        # Send data bits
        for bit in data:
            self.data_pin.value(bit)
            time.sleep_ms(10)
        
        time.sleep(duration)
        self.tx_pin.off()
        self.is_transmitting = False
        print(f"Transmitted: {data}")
        
    def receive(self, timeout=5):
        """Receive RF signal"""
        start = time.time()
        received_data = []
        
        while time.time() - start < timeout:
            if self.rx_pin.value():
                received_data.append(1)
            else:
                received_data.append(0)
            time.sleep_ms(10)
        
        return received_data
        
    def get_signal_strength(self):
        """Read signal strength from ADC"""
        return self.adc.read()
        
    def scan_frequencies(self):
        """Scan common ISM band frequencies"""
        frequencies = [433, 868, 2400]
        results = {}
        
        for freq in frequencies:
            self.set_frequency(freq)
            time.sleep_ms(100)
            signal = self.get_signal_strength()
            results[freq] = signal
            print(f"Freq {freq}MHz: Signal={signal}")
        
        return results


class HomeRFBridge:
    def __init__(self, ssid=None, password=None):
        self.rf = RFController()
        self.wifi = None
        
        if ssid and password:
            self.connect_wifi(ssid, password)
        
    def connect_wifi(self, ssid, password):
        """Connect to WiFi network"""
        self.wifi = network.WLAN(network.STA_IF)
        self.wifi.active(True)
        self.wifi.connect(ssid, password)
        
        timeout = 10
        start = time.time()
        while not self.wifi.isconnected() and time.time() - start < timeout:
            time.sleep(1)
        
        if self.wifi.isconnected():
            print(f"WiFi connected: {self.wifi.ifconfig()}")
        else:
            print("WiFi connection failed")
    
    def web_server(self, port=80):
        """Start simple web server for RF control"""
        if not self.wifi or not self.wifi.isconnected():
            print("WiFi not connected")
            return
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', port))
        server.listen(1)
        print(f"Web server listening on port {port}")
        
        while True:
            try:
                conn, addr = server.accept()
                request = conn.recv(1024).decode()
                
                response = self.handle_request(request)
                conn.sendall(response)
                conn.close()
            except Exception as e:
                print(f"Server error: {e}")
    
    def handle_request(self, request):
        """Handle HTTP requests for RF control"""
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        
        if "transmit" in request:
            self.rf.transmit([1, 0, 1, 0, 1, 1, 0, 1])
            response += "<html><body>Transmitting...</body></html>"
        elif "scan" in request:
            results = self.rf.scan_frequencies()
            response += f"<html><body>Scan Results: {results}</body></html>"
        else:
            response += "<html><body><h1>RF Control</h1>"
            response += "<a href='/?transmit'>Transmit</a><br>"
            response += "<a href='/?scan'>Scan</a></body></html>"
        
        return response.encode()


# Main execution
if __name__ == "__main__":
    # Initialize RF Controller
    rf_ctrl = RFController()
    
    # Example: Set frequency and power
    rf_ctrl.set_frequency(433)
    rf_ctrl.set_power(80)
    
    # Example: Transmit data
    rf_ctrl.transmit([1, 0, 1, 1, 0, 0, 1, 0], duration=0.5)
    
    # Example: Scan frequencies
    results = rf_ctrl.scan_frequencies()
    
    # Optional: Start WiFi bridge for remote control
    # bridge = HomeRFBridge(ssid="YOUR_SSID", password="YOUR_PASSWORD")
    # bridge.web_server()
    
    print("RF Control ready")
