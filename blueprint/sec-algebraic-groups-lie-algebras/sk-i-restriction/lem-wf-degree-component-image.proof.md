+++
kind  = "proof"
of    = "lem-wf-degree-component-image"
+++
The elements of $\deg^{-1}(m)$ are the elements of $W(X_0)$ of degree
$m$, namely the coset $\pi_1(X)s^m$ of the degree homomorphism of
[def-wf-weil-group]. Since the representation $\rho$ of
[def-wf-fundamental-representation] is a homomorphism by
[lem-wf-weil-fundamental-representation], its image is
$\rho(\pi_1(X))\rho(s)^m$. Right translation by the fixed matrix
$\rho(s)^m$ is a homeomorphism of $\operatorname{GL}(V)$ for the
Zariski topology, so it carries the closure of
$\rho(\pi_1(X))$ to the closure of the translate, i.e. $\overline{\rho(\deg^{-1}(m))}^{\mathrm{Zar}} =H_{\mathrm{geom}}\rho(s)^m$ with $H_{\mathrm{geom}}$ as in
[def-wf-geometric-monodromy-group]. On the other hand
$G^{[m]}=H_{\mathrm{geom}}\times\{m\}$ by
[def-wf-degree-components], and the matrix map of
[def-wf-arithmetic-monodromy-extension] sends $(h,m)$ to
$h\rho(s)^m$, so the image of $G^{[m]}$ is the same set
$H_{\mathrm{geom}}\rho(s)^m$. The two descriptions therefore agree.
