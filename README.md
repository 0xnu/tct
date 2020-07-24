## Tails Coding Test

"Tailored dog food, based on your dog's unique nutritional needs and delivered to your door each month. Start your trial today." - [Tails](https://www.tails.com).

### Development

Fire up your development environment

```bash
# Install libraries and dependencies (macOS Workflow)
python3 -m venv venv_dev_tails
source venv_dev_tails/bin/activate
pip3 install -r pip/dev.txt
flask run

# Install libraries and dependencies (Windows Workflow)
py -3 -m venv_dev_tails dev
venv_dev_tails\Scripts\activate.bat
pip3 install -r pip/dev.txt
flask run

# Application is accessible here
http://127.0.0.1:5000 or http://localhost:5000

# Store Endpoint is accessible here
http://127.0.0.1:5000/stores or  http://localhost:5000/stores
```

### The person responsible if something goes wrong a.k.a The Author 😉 

- **Finbarrs Oketunji** - _Backend Software Engineer_ > _[0xnu](https://github.com/0xnu)_


### License

The script is published under [BSD 3-Clause License](LICENSE).


### Copyright

(c) 2020 [Tailsco Ltd](https://www.tails.com).