## 2024-05-24 - O(N*M) extraction from PCAP
**Learning:** `pwnagotchi.utils.extract_from_pcap` reads the entire PCAP file multiple times using `scapy.sniff`, resulting in an O(N*M) runtime complexity (where N is the number of packets and M is the number of fields to extract). This is a known performance bottleneck.
**Action:** Rewrite `extract_from_pcap` to read the PCAP file only once using `scapy.utils.PcapReader` (or a single `sniff` if necessary, but `PcapReader` is an iterator and better for memory) and extract all requested fields in a single pass.
