+++
kind = "proof"
of = "det-finite-window-unbounded"
+++
*Left completeness.* By [sk-thm-pe-weakly-contractible-basis] and [sk-prop-pe-products], products of
$\Lambda_X$-modules are exact and products in $\D(X_{\mathrm{proét}},\Lambda)$ are termwise; by
[sk-prop-pe-left-complete], $L\cong R\varprojlim_n\tau_{\geq-n}L$, where
$R\varprojlim_nL_n=\fib\bigl(\prod_nL_n\xrightarrow{1-\mathrm{shift}}\prod_nL_n\bigr)$ for the tower
$L_n=\tau_{\geq-n}L$.

*Milnor sequence.* Applying $\Hom(C,-)$, which takes products to products, to the defining triangle
gives a long exact sequence whose relevant part is

$$
\prod_n\Hom(C,L_n[-1])\xrightarrow{1-\mathrm{shift}}\prod_n\Hom(C,L_n[-1])\to\Hom(C,L)\to
\prod_n\Hom(C,L_n)\xrightarrow{1-\mathrm{shift}}\prod_n\Hom(C,L_n),
$$

i.e. $0\to\varprojlim^1_n\Hom(C,L_n[-1])\to\Hom(C,L)\to\varprojlim_n\Hom(C,L_n)\to0$.

*Right term.* Each $L_n$ is bounded, lies in $\Dic(X,\Lambda)$ ([sk-cor-ambient-ind-derived]), and has
cohomology in degrees $\leq-d_C-1$, so $\Hom(C,L_n)=0$ by [det-finite-window-bounded].

*Left term.* The fiber of $L_{n+1}\to L_n$ is $H^{-n-1}(L)[n+1]$, so there is an exact sequence

$$
\Hom(C,H^{-n-1}(L)[n])\to\Hom(C,L_{n+1}[-1])\to\Hom(C,L_n[-1])\to\Hom(C,H^{-n-1}(L)[n+1]),
$$

whose outer terms are $\Ext^{n}(C,H^{-n-1}L)$ and $\Ext^{n+1}(C,H^{-n-1}L)$. For $n>d_C$ both vanish by
[sk-cor-ind-heart-ii], so the transition maps of the tower $G_n=\Hom(C,L_n[-1])$ are isomorphisms for
$n>d_C$.

*Vanishing of $\varprojlim^1$.* Let $(y_n)\in\prod_nG_n$; we solve $x_n-t(x_{n+1})=y_n$ where
$t\colon G_{n+1}\to G_n$ is the transition. Choose $N>d_C$. Since $t\colon G_{n+1}\to G_n$ is bijective for $n\geq N$,
identify all $G_n$ ($n\geq N$) with $G_N$ along these bijections; the equation becomes $x_n=x_{n+1}+y_n$ in $G_N$, solved by $x_N=0$ and
$x_{n+1}=x_n-y_n$ for $n\geq N$. For $n<N$ put $x_n=y_n+t(x_{n+1})$ successively for
$n=N-1,\dots,0$. Hence $1-\mathrm{shift}$ is surjective and $\varprojlim^1G_n=0$.

Therefore $\Hom(C,L)=0$.
