+++
kind = "proof"
of = "lemma-positivity-convergence"
order = 1160
+++
We compare coefficients and then apply Cauchy's estimate. To compare, write
$f_j=\sum_na_{j,n}t^n$ and $L=\sum_nA_nt^n$. Since the product is
coefficientwise locally finite, $A_n$ is already the coefficient of $t^n$ in a
finite subproduct containing $f_j$, which is $f_j$ times
a series $g$ with constant coefficient one and nonnegative coefficients.
The coefficient of $t^n$ in $f_jg$ is $a_{j,n}$ plus a sum of products of
nonnegative numbers, so that $0\le a_{j,n}\le A_n$; positivity enters
only here.  Next, for every $0<r<R$, Cauchy's estimate gives
$|A_n|\le C_rr^{-n}$. Hence the radius of convergence of $f_j$ is at least
$r$ for every such $r$, and so at least $R$.  A zero of $P_j$ in the disc
would be a pole of $f_j=1/P_j$, which is impossible.
