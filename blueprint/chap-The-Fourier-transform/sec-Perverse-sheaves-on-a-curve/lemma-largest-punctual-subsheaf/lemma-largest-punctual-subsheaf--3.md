+++
id = "lemma-largest-punctual-subsheaf--3"
kind = "lemma"
title = "The punctual kernel and the unit"
order = 1245004
aliases = ["bp-r384-3"]
lean = ["AlgebraicGeometry.WeilSheaf.support_finite_kernel_unit_app", "AlgebraicGeometry.WeilSheaf.mono_unit_app"]
uses = ["definition-weil-structure", "definition-punctual-sheaf", "proposition-topos-functoriality", "lemma-largest-punctual-subsheaf--2"]
+++
The maximality assertion is bypassed by the Lean route, which uses the
following punctuality and injectivity statements.

Let $k_0=\Fq$, let $\ell$ be a prime with $\ell\nmid q$, let
$j:U_0\hookrightarrow\Aone_{k_0}$ be a dense open immersion, and let $F$
be a Weil $\overline{\mathbf Q}_\ell$-sheaf on $\Aone_{k_0}$. The kernel

$$
F_{\rm p}=\ker(F\longrightarrow j_*j^*F)
$$

is punctual, without any assumption that $j^*F$ is lisse. If $F$ has no
nonzero punctual subsheaf, the unit $F\to j_*j^*F$ is a monomorphism.
