+++
id = "example-trace-function-squaring"
kind = "example"
title = "The squaring map"
order = 1020
+++
Let $q$ be odd, let $f_0:\mathbf A^1_{\mathbf F_q}\to\mathbf A^1_{\mathbf F_q}$
be $x\mapsto x^2$, and let $K=\Lambda_X$ with its constant Weil structure, so
that $t_{K,m}=1$. The fibre of $f_0$ over $y\in\mathbf F_{q^m}$ has
$1+\chi_m(y)$ rational points, where $\chi_m$ is the quadratic character of
$\mathbf F_{q^m}^*$, extended by $\chi_m(0)=0$. Hence

$$
t_{Rf_!\Lambda,m}(y)=1+\chi_m(y).
$$

The trace function of $Rf_!\Lambda$ is not constant, although the sheaf we
pushed forward is. Over $\mathbf G_m$ the map is a finite étale double cover.
The term $\chi_m(y)$ records whether the fibre over $y$ splits into two
rational points or is a single point of degree $2$. Summing over $y$ recovers the
trace formula on the source. Since $\chi_m$ takes the values $\pm1$ equally
often on $\mathbf F_{q^m}^*$, the sum is $q^m=\#\mathbf A^1(\mathbf F_{q^m})$.
