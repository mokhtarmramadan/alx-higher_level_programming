#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
if __name__ == "__main__":
    import urllib.request

    url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    try:
        with urllib.request.urlopen(url) as response:
            # Read the response content as bytes
            content_bytes = response.read()
            print(f'Body response:\n  - type: {type(content_bytes)}\n\
  - content: {content_bytes}')

            # Decode the bytes content to UTF-8
            utf8_content = content_bytes.decode('utf-8')
            print(f'  - utf8 content: {utf8_content}')

    except urllib.error.URLError as e:
        print(f'Error: {e.reason}')
    except urllib.error.HTTPError as e:
        print(f'HTTP Error: {e.code}')
