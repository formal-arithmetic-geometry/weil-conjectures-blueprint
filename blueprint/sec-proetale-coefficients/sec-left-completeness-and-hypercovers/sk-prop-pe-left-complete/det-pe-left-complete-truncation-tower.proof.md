+++
kind = "proof"
of = "det-pe-left-complete-truncation-tower"
+++
*1.* The object $\tau_{\geq-n}K$ lies in degrees $\geq-n$, so its $H^q$ vanishes for $q<-n$,
i.e. for $n<-q$. For $q\geq-n$ the truncation map $K\to\tau_{\geq-n}K$ induces an isomorphism
on $H^q$ (represent $K$ by a complex; $\tau_{\geq-n}K$ is the quotient complex
$0\to K^{-n}/\operatorname{im}d^{-n-1}\to K^{-n+1}\to\cdots$).

*2.* Write $G_n=H^q(\tau_{\geq-n}K)$ and let $c_n\colon H^q(K)\to G_n$ be the maps induced by
the truncation maps; they are compatible with the transitions. By 1, $G_n=0$ for $n<N$ and
$c_n$ is an isomorphism for $n\geq N$. Let $\rho_n=c_n^{-1}$ for $n\geq N$ and $\rho_n=0$
otherwise. The map $\sigma\colon\prod_nG_n\to\prod_nG_n$ with components
$y\mapsto-c_n\bigl(\sum_{N\leq k<n}\rho_k(y_k)\bigr)$ satisfies $(1-T)\circ\sigma=\mathrm{id}$:
in component $n\geq N$ this is $-c_n(\sum_{N\le k<n}\rho_ky_k)+c_n(\sum_{N\le k\le n}\rho_ky_k)
=y_n$, and components $n<N$ vanish. Hence $1-T$ is a split epimorphism and its cokernel
$R^1\varprojlim_nG_n$ vanishes.

A cone $(L,(\ell_n))$ over the tower $(G_n)$ factors uniquely through $H^q(K)$ via
$\rho_N\circ\ell_N$: for $n\geq N$ the transition maps between the $G_n$ are isomorphisms
compatible with the $c_n$, and for $n<N$ the terms vanish. Hence $(H^q(K),(c_n))$ is a limit
cone.
