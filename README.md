# SimpleLaGrangeErrorBoundCalculator

Description: A simple python script for calculating the la grange error bound and degree of common maclaurin/taylor series, sin(x), cos(x), e^x, ln(x)

usage: LaGrangeErrorBound.py [-h] [-c CENTER] [-d degree] [-e ERROR]
                             function x-value

Calculate the La Grange Bound Error or the degree of polynomial required to
attain a certain error for Common Functions

positional arguments:
  function              The common function you wish to approximate with a
                        maclaurin/taylor series. The current version supports
                        exponentials ("exp"), logarithms ("log"), and
                        oscillating functions ("sin" or "cos")
  x-value               The x value you wish to approximate

optional arguments:
  -h, --help            show this help message and exit
  -c CENTER, --center CENTER
                        The value the taylor series is centered at, if you are
                        using a taylor series
  -d degree, --degree degree
                        The degree of the maclaurin or taylor series
                        polynomial you are using
  -e ERROR, --error ERROR
                        The error value as a decimal, the return value will be
                        the degree polynomial you need to use to achieve at
                        least this level of precision
