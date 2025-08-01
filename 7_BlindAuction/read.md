The goal is to build a blind auction program.

Demo
https://appbrewery.github.io/python-day9-demo/

Clearing the Output
There are several ways of clearing the output. The easiest is to simply print "\n" many times so that the output scrolls down many lines.

e.g.
This will add 20 new lines to the output</br>

print("\n" * 20)</br>
Functionality</br>
Each person writes their name and bid.</br>
The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines)</br> then loops back to asking name and bid.
Each person's name and bid are saved to a dictionary.</br>
Once all participants have placed their bid, the program works out who has the highest bid and prints it.</br>
 Hint 1 </br>
Try writing out a flowchart to plan your program.</br>
 Hint 2 </br>
The values that come from the input() function are Strings, you'll need to use the int() function to convert it to a number.</br>
Flowchart</br>
If you want to see my flowchart, you can download it here. </br>
https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Blind%2520Auction%2520Flow%2520Chart%23R3VnbcpswEP0aPzYDCLB5tHNrZ9pMpu6kzaMMilEDiBHyLV%252FfFYirHMdp7JD4JUGrXV3Ont2V5AE6j9fXHKfhDxaQaGAZwXqALgaWZRqmAf%252BkZFNIHM8qBHNOA6VUC6b0iZSWSrqgAclaioKxSNC0LfRZkhBftGSYc7Zqqz2wqD1riudEE0x9HOnS3zQQoZK6jl13fCV0HpZTm65X9MS41FZbyUIcsFVDhC4H6JwzJoqveH1OIoleCUxhd%252FVMb7UyThKxj8Hs4R5fx%252BMlu%252F52dxPepdM7H31BxShLHC3UjtVixaaEgASAiGoyLkI2ZwmOLmvphLNFEhA5jQGtWuc7YykITRD%252BJUJslHvxQjAQhSKOVG8xp5zo2b0pUcYW3Cc7NlSSBPM5ETv0rMoDwF3CYiL4Buw4ibCgy%252FY6sCLRvNKrYYYPhfQrUDc11Ke%252Fxj9%252FadDXwEqUViEVZJrifP8riLdtIC4JF2S9G0Z928rAHimuqmi1VXNVU99TorBBemQcCSfn1Nhp7clOu092Wjo7Q0hclhEBcDKJchbn6VWcpZsPx1mvZ84OT42z9p6cdfvkrK2hPs4e84LP4e8NjokcIUkXon%252FCOk6LsKajM9a0t1DWPhZlvVOjrLsnZUd9UtbdSdkJ2FrGLaew0Y%252FG2OpI2xtjTf0E9ckp%252B1YqKtNbRmHmynOO1fYcGnU8UoSIsuo4pVrG%252F%252FtppHM8COqEjJOgojqsQB4usLwsUl9QcESOAKwUIjmU6o9kUxnlQ54NLBfHkvDJLEsrh%252FQZKmh41gmWLQcSc%252BjoweIcLVhGfcQGWVPxR5nL7%252FuG%252FGLd6LjYlI0EdpubAISqed%252Fsq83yVml3wCg00Z6VwxweIl7HnONNQyGVcZg9H872yGxxy%252B5e%252BTv6yHN26cNHsYKDxnwFdi90Mxt0Uzw6CcI1noz6eLDQ34mKwwp9KLIzz9N5%252FpfJ5kCu141gR5MZNNy5%252FFpkhMtsvgplpl%252FhnKp51p%252FJEtBN3SGLZ4usp7RdVcqX0na3oh4Oc%252F2AeE8yDSbYtGjjgSM6T%252BDbh82DJ9BEQkN9HI1VR0yDoIg6ktEnPMuHksRW%252BQfGdSYD50KOBYGWFTF3IKiRZ7dzkmFrQG87S1pHw9nrtTxWOeo1BbKVrerk9Q75arhnvnrrC9b2gmZ1HnvQcL%252Fz7GsLbbdwOvbuQttd12v1zeE7FGZTf5o6jwjm1fk68zkhiZ6I3%252FkMjZzOK%252FSWVLztSe9ot80y9TSAu6L5LaTALYQ1kEyUdQyuMlVX%252ByqT2wTEj4pKCSpx%252B4azokkii2fPHnCGL3vA9LYUQ%252FdoLrA0F9ywT18LXdTB2dBxRoephdCsf2osMkr9iy26%252FAc%253D#