package main

import (
	"fmt"
	"os"
	"os/exec"
)

// BlackHoleIP drops an IP into a null route (The Void)
func BlackHoleIP(ip string) {
	fmt.Printf("ARES: Commencing Black Hole for target %s...\n", ip)
	
	// This command tells the Linux kernel: "Any traffic from this IP goes to nowhere."
	// It is faster and more efficient than a standard firewall rule.
	cmd := exec.Command("sudo", "ip", "route", "add", "blackhole", ip)
	
	err := cmd.Run()
	if err != nil {
		fmt.Printf("ARES ERROR: Failed to engage Void for %s. (Are you root?)\n", ip)
		return
	}
	fmt.Printf("ARES: %s has entered the Void.\n", ip)
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: ./void <ip_address>")
		return
	}
	target := os.Args[1]
	BlackHoleIP(target)
}
