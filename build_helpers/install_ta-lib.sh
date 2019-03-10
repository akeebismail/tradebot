if [ ! -f "/usr/local/lib/libta_lib.a" ]; then
  tar zxvf ta-lib-0.4.0-src.tar.gz
  cd ta-lib \
  && sed -i.bak "s|0.00000001|0.000000000000000001 |g" src/ta_func/ta_utility.h \
  && ./configure \
  && make \
  && which sudo && sudo make install || make install \
  && cd ..
else
  echo "TA-lib already installed, skipping installation"
fi