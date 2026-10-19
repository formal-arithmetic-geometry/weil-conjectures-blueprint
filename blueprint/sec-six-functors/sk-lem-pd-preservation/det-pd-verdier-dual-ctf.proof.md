+++
kind = "proof"
of = "det-pd-verdier-dual-ctf"
uses = ["det-pd-dualizing-complex-ctf", "det-thm-sf-ctf-stability-internal-hom"]
+++
By [det-pd-dualizing-complex-ctf], $\omega_{X,\Lambda}\in\Dctf(X,\Lambda)$.
For $K,L\in\Dctf(X,\Lambda)$ the internal Hom $\cHom_\Lambda(K,L)$ lies in
$\Dctf(X,\Lambda)$ by [det-thm-sf-ctf-stability-internal-hom]. Taking
$L=\omega_{X,\Lambda}$ gives $\mathbb D_XK\in\Dctf(X,\Lambda)$.

The functor $\cHom_{\Lambda_X}(-,\omega_{X,\Lambda})$ on
$D(X_{\mathrm{pro\acute et}},\Lambda)$ is exact and contravariant: it carries
distinguished triangles to distinguished triangles and commutes with shifts up
to the sign change of the shift. Since $\Dctf(X,\Lambda)$ is a full
triangulated subcategory, the restriction is an exact functor
$\Dctf(X,\Lambda)^{\mathrm{op}}\to\Dctf(X,\Lambda)$.
