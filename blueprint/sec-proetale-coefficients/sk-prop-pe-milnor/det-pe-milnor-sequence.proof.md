+++
kind = "proof"
of = "det-pe-milnor-sequence"
+++
The distinguished triangle
$R\varprojlim_nF_n\xrightarrow{p}\prod_nF_n\xrightarrow{1-T}\prod_nF_n\to R\varprojlim_nF_n[1]$
gives the long exact sequence

$$
\cdots\to H^{q-1}\bigl(\textstyle\prod_nF_n\bigr)\xrightarrow{H^{q-1}(1-T)}
H^{q-1}\bigl(\textstyle\prod_nF_n\bigr)\to H^q\bigl(R\varprojlim_nF_n\bigr)\xrightarrow{H^qp}
H^q\bigl(\textstyle\prod_nF_n\bigr)\xrightarrow{H^q(1-T)}H^q\bigl(\textstyle\prod_nF_n\bigr)\to\cdots,
$$

hence the short exact sequence
$0\to\coker H^{q-1}(1-T)\to H^q(R\varprojlim_nF_n)\to\ker H^q(1-T)\to0$. Countable products
in $\mathcal C$ are exact, so by [det-pe-products-derived] products in $D(\mathcal C)$ are
termwise and $H^q(\prod_nF_n)=\prod_nH^q(F_n)$; under this identification $H^q(1-T)$ is $1-T$
for the tower $(H^q(F_n))_n$. Its kernel consists of the families $(h_n)$ with
$h_n=t_n(h_{n+1})$, i.e. it is $\varprojlim_nH^q(F_n)$, and the map to it is induced by the
legs of the cone. This proves 1.

For 2, the terms $M_n$ lie in degree $0$, so the product $\prod_nM_n$ lies in degree $0$ and,
by the long exact sequence, $R\varprojlim_nM_n$ lies in degrees $[0,1]$. In the sequence of 1,
for $q=0$ the cokernel term is $0$ and the limit term is $\varprojlim_nM_n$; for $q=1$ the
cokernel term is $R^1\varprojlim_nM_n$ and the limit term is $0$. Statement 3 is 1 combined
with the definition of $R^1\varprojlim$ applied to the tower $(H^{q-1}(F_n))_n$.
