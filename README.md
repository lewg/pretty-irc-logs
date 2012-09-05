# Pretty IRC Logs

A simple [Flask](http://flask.pocoo.org/) application that uses [Pygments](http://pygments.org/) to highlight your IRC logs, and [Twitter's Bootstrap](http://twitter.github.com/bootstrap/index.html) to make the page full of responsive goodness. Admittedly, tailored exactly to my specific use case, but who knows, maybe your setup is just like mine! 

## Setup

Use `easy_install` to install the dependencies:

    easy_install Flask
    easy_install Pygments

In `log_highlighter.py` adjust `base_url`, `base_path` and `channels` to your setup.

Run `python log_highlighter` and visit `http://localhost:5000`

## License

Copyright 2012 Lewis J. Goettner, III

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.