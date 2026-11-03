+++
kind  = "proof"
of    = "lem-sf-class-compact-support-comparison"
+++
Fix the compactification $(j,p)$: $Rf_{!,n}$ is the candidate of
[def-compact-support-direct-image-detailed] attached to it, and $Rf_!^{\Et}$
is the étale candidate attached to the same one, so it suffices to
compare them there. The complex $K$ comes from the étale site with a
witness in the sense of
[def-weil-pbc-etale-origin-witness]. On the pro-étale
site $j_!$ is the exact
extension by zero of
[def-weil-extension-by-zero], on the étale site it is the exact
extension by zero of
[def-weil-pbc-extension-by-zero], and
[lem-cbc-proetale-extension-zero-comparison] identifies them along the
comparison morphism of [def-weil-pbc-site-comparison-morphism]:

$$
\nu_{\overline X}^*j_!^{\Et}\xrightarrow{\ \sim\ }j_!\nu_X^* .
$$

That identification is natural in the coefficient sheaf and both functors
are exact, so, applied degreewise to the bounded-below complex $G$, it
gives an isomorphism of complexes
$\nu_{\overline X}^*j_!^{\Et}G\cong j_!\nu_X^*G$, compatible with the
differentials. The witness identifies $K$ with $\nu_X^*G$, whence
$Rf_{!,n}K\cong Rp_*j_!\nu_X^*G$. The proper morphism $p$ is of finite
type, hence quasi-compact and quasi-separated, and $j_!^{\Et}G$ is a
bounded-below complex on $\overline X_{\Et}$, so the comparison direct
image [prop-weil-pbc-comparison-direct-image] applied to $u=p$ and
$L=j_!^{\Et}G$ gives

$$
Rp_*\bigl(\nu_{\overline X}^*j_!^{\Et}G\bigr)
\cong\nu_Y^*\bigl(Rp_{\Et,*}j_!^{\Et}G\bigr)
=\nu_Y^*\bigl(Rf_!^{\Et}G\bigr).
$$

Composing the two isomorphisms gives the displayed comparison. Naturality
in the witness is the naturality of the extension-by-zero comparison, of
the comparison direct image, and of the witness identification. No
constructibility is used, and the étale compact-support functor is the
candidate of [def-amb-etale-compact-support] attached to the same
compactification: it is the functor denoted $Rf_!$ in the
ambient-smooth-duality chapter and written $Rf_!^{\Et}$ here to separate
it from the pro-étale functor.
