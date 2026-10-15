+++
kind = "proof"
of = "det-pe-milnor-sequence"
+++
For a map of complexes $\varphi\colon A\to B$, the triangle
$\operatorname{Cone}(\varphi)[-1]\to A\xrightarrow{\varphi}B\to\operatorname{Cone}(\varphi)$
gives the long exact sequence

$$
\cdots\to H^{q-1}(A)\xrightarrow{H^{q-1}\varphi}H^{q-1}(B)\to
H^q(\operatorname{Cone}(\varphi)[-1])\to H^q(A)\xrightarrow{H^q\varphi}H^q(B)\to\cdots,
$$

hence the short exact sequence
$0\to\coker H^{q-1}\varphi\to H^q(\operatorname{Cone}(\varphi)[-1])\to\ker H^q\varphi\to0$.
Apply this with $A=B=\prod_nK_n$ and $\varphi=1-T$. By [det-pe-products-derived],
$H^q(\prod_nK_n)=\prod_nH^q(K_n)$, and under this identification $H^q(1-T)$ is $1-T$ for
the tower $(H^q(K_n))_n$. Its kernel consists of the families $(h_n)$ with
$h_n=t_n(h_{n+1})$, i.e. it is $\varprojlim_nH^q(K_n)$ (limits of sheaves being computed
sectionwise). This proves 1.

For 2, $\prod_nM_n$ is concentrated in degree $0$, so $\operatorname{Cone}(1-T)[-1]$ is the
two-term complex $\prod_nM_n\xrightarrow{1-T}\prod_nM_n$ in degrees $0$ and $1$. Its
$H^0$ is $\ker(1-T)=\varprojlim_nM_n$, its $H^1$ is $\coker(1-T)$, and all other
cohomology vanishes. Statement 3 is 1 combined with 2 applied to the tower
$(H^{q-1}(K_n))_n$.
