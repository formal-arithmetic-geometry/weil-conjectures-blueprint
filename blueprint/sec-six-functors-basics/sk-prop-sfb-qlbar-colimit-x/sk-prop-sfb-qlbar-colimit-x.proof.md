+++
kind  = "proof"
of    = "sk-prop-sfb-qlbar-colimit-x"
uses = ["sk-prop-sfb-qlbar-colimit-point", "sk-def-sfb-pullback-from-point", "def-sfb-integers-to-subfield"]
+++
*First isomorphism.* On the point, $\underline{\cO_E}$ is represented by the profinite set
$\cO_E=\varprojlim_n\cO_E/\pi_E^n$, so its pullback to $X$ is represented by the
pro-étale $X$-scheme $\varprojlim_n\coprod_{\cO_E/\pi_E^n}X$. By the Yoneda lemma the sheaf
this scheme represents is $\varprojlim_n(\cO_E/\pi_E^n)_X$, and the ring structures match.
Working with the representing scheme is what makes this easy: $p_X^*$ itself does not
commute with inverse limits in general. Details: [det-prop-sfb-qlbar-colimit-x-integral-limit].

*Second isomorphism.* A continuous map from a profinite set to $E$ has compact image, hence
lands in $\ell^{-m}\cO_E$ for some $m$; thus $\underline E=\underline{\cO_E}[1/\ell]$ on the
point. Since $p_X^*$ commutes with colimits, and inverting $\ell$ is a filtered colimit, we
get the second isomorphism, along the map $\cO_{E,X}\to E_X$ of
[def-sfb-integers-to-subfield]. Details: [det-prop-sfb-qlbar-colimit-x-invert-ell].

*Third isomorphism.* In the same way, $\underline{\Qlb}=\varinjlim_E\underline E$ on the
point ([sk-prop-sfb-qlbar-colimit-point]), and $p_X^*$ preserves this colimit. The ring
objects $E_X$ and $\QbarX$ are [def-sfb-subfield-coefficient-ring] and
[def-sfb-qlbar-coefficient-ring], and the colimit cocone is [def-sfb-qlbar-x-cocone]; it is
the image under the left adjoint $p_X^*$ of a colimit cocone, hence a colimit cocone.

*Compatibility with inverse image.* All three are built from $p_X^*$ (and, for the first,
from the representing scheme, whose formation commutes with base change), so they are
compatible with pullback. Details: [det-prop-sfb-qlbar-colimit-x-pullback].
