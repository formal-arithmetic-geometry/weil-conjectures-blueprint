+++
kind = "proof"
of = "det-pe-continuous-cohomology-milnor"
+++
Put $K_n=R\Gamma(X_{\Proet},F_n)$. By [det-pe-continuous-cohomology-limit],
$R\Gamma(X_{\Proet},F)$ is the fibre of $1-\text{shift}\colon\prod_nK_n\to\prod_nK_n$.
Products are exact in $\Ab$, so $H^q(\prod_nK_n)=\prod_nH^q(K_n)$, and the long
exact sequence of the triangle gives

$$
\prod_nH^{q-1}(K_n)\xrightarrow{1-\text{shift}}\prod_nH^{q-1}(K_n)\to
H^q(R\Gamma(X,F))\to\prod_nH^q(K_n)\xrightarrow{1-\text{shift}}\prod_nH^q(K_n).
$$

The kernel of $1-\text{shift}$ on $\prod_nH^q(K_n)$ is $\varprojlim_nH^q(K_n)$ and
its cokernel on $\prod_nH^{q-1}(K_n)$ is $\varprojlim^1_nH^{q-1}(K_n)$, by the
standard description of $\varprojlim$ and $\varprojlim^1$ of a sequence; this is
the displayed sequence (compare [det-pe-milnor-sequence]).

If the groups $A_n$ of a sequence are finite, then $\varprojlim^1A_n=0$: for fixed $n$
the images of $A_m\to A_n$, $m\geq n$, form a descending chain of subgroups of a
finite group, which stabilizes, so the sequence satisfies Mittag-Leffler, and
$\varprojlim^1$ of a Mittag-Leffler sequence vanishes.
