+++
id = "lem-zla-counting-log"
kind = "lemma"
title = "Counting logarithm equals trace logarithm"
order = 993
uses = ["def-zla-trace-datum"]
+++
For a finite cohomological trace datum,

$$
\sum_{n\geq1}N_n\frac{T^n}{n}
=\sum_{n\geq1}\left(\sum_{i=0}^r(-1)^i\Tr(F_i^n\mid V_i)\right)\frac{T^n}{n}
\qquad\text{in }TE[[T]].
$$

## Proof

The two series are compared coefficientwise; in degree $n$ the assertion is
the image in $E$ of the equality (iii) of [def-zla-trace-datum] divided by
the invertible integer $n$. The left-hand side is the coefficientwise scalar
extension along $\mathbf Q\to E$ of a series with rational coefficients.
