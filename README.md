Cocoapod Badges [![Build Status](https://travis-ci.org/fjcaetano/cocoapod-badges.png)](https://travis-ci.org/fjcaetano/cocoapod-badges)
===============

[![NSStringMask](http://cocoapod-badges.herokuapp.com/v/NSStringMask/badge.png)](http://cocoadocs.org/docsets/NSStringMask) NSStringMask's latest version badge

Cocoapod Badges are status badges to inform a pod's latest version deployed to [Cocoapods] through their [simple API](https://github.com/CocoaPods/cocoapods.org/commit/8ef51c7890c33ad899e8130b9e778c740c5c7f61).

The badges are created with a `SVG` file, thanks to [olivierlacan/shields](https://github.com/olivierlacan/shields) repo that provides badges to:

- [Code Climate](https://codeclimate.com/changelog/510d4fde56b102523a0004bf)
- [Coveralls](https://coveralls.io/r/kaize/nastachku)
- [Gemfury/RubyGems](http://badge.fury.io/)
- [Gemnasium](http://blog.tech-angels.com/post/43141047457/gemnasium-v3-aka-gemnasium)
- [Travis CI](http://about.travis-ci.org/docs/user/status-images/)

No images are generated. The badges are `SVG` files compiled by the browser. They may be saved, but if you look at their source code, you'll be able to see the `SVG` xml file.

The "badge service" is hosted at [Heroku](https://www.heroku.com/)

# Usage

Just replace the `$PODNAME` on both URLs and the badge will automatically fetch the info.

**_ATTENTION_**: The `$PODNAME` is case sensitive, since [Cocoapods] has differentiation! In case of unexpected issues, the badges will display "error".

## Version Badge

Displays the pod's latest version available.

	http://cocoapod-badges.herokuapp.com/v/$PODNAME/badge.png

[![NSStringMask](http://cocoapod-badges.herokuapp.com/v/NSStringMask/badge.png)](http://cocoadocs.org/docsets/NSStringMask)

## Platforms Badge

For this to be available, the pod must provide this information, which is optional. If it's not set, the badge will display "error", even though `$PODNAME` may be correct!

	http://cocoapod-badges.herokuapp.com/p/$PODNAME/badge.png

iOS | OSX | iOS/OSX | error
--- | --- | ------- | -----
![ios](http://cocoapod-badges.herokuapp.com/p/AKLocationManager/badge.png) | ![osx](http://cocoapod-badges.herokuapp.com/p/DDQuicklookAdditionalViews/badge.png) | ![ios/osx](http://cocoapod-badges.herokuapp.com/p/AFNetworking/badge.png) | ![error](http://cocoapod-badges.herokuapp.com/p/Kiwi/badge.png)

## Deprecation Warning

This is a new version of Cocoapod Badges! The previous version (case insensitive) is still available at `/v1/` for continuity reasons but it's **deprecated** and its support will stop! All you have to do is fix upper and lower case letters on your badge's URL.

# License

cocoapod-badges is licensed under the MIT License:

Copyright (c) 2013 Flávio Caetano ([http://flaviocaetano.com](http://flaviocaetano.com))

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[Cocoapods]: http://cocoapods.org