+++
kind  = "proof"
of    = "lem-wf-degree-component-image"
+++
By [d-monodromy] every element of $W$ of degree $m$ has the form $us^m$
with $u\in P$, so $\deg^{-1}(m)$ is the coset $Ps^m$. Since $\rho$ is a
homomorphism, its image is $\rho(P)F^m$. Right translation by the fixed
matrix $F^m$ is an automorphism of the variety $\operatorname{GL}_n$, so
it carries the closure $H$ of $\rho(P)$ to the closure of the
translate, i.e. $\overline{\rho(\deg^{-1}(m))}^{\mathrm{Zar}}=HF^m$.
On the other hand $G^{[m]}=H\times\{m\}$ by
[def-wf-degree-components], and the matrix map of
[def-wf-arithmetic-monodromy-extension] sends $(h,m)$ to $hF^m$, so the
image of $G^{[m]}$ is the same set $HF^m$. The two descriptions
therefore agree.
