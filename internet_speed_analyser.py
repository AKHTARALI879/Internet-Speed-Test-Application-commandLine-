import speedtest

internet_check = speedtest.Speedtest()

print("Loading Servers List...")
internet_check.get_servers()
print("Choosing best server... ")
best_country = internet_check.get_best_server()

print(f"Found:. {best_country['host']} located in {best_country['country']}")

print("Performing downloading test.... ")
download_result = internet_check.download()
print("Performing uploading test... ")
upload_result = internet_check.upload()
ping_result = internet_check.results.ping

print(f"Download Speed: {download_result / 1024 / 1024:.3f}Mbps")
print(f"Upload Speed: {upload_result / 1024 / 1024:.3f}Mbps")
print(f"Ping: {ping_result}ms")
