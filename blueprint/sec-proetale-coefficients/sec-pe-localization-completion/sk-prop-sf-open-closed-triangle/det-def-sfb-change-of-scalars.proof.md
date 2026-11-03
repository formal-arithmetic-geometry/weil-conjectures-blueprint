+++
kind  = "proof"
of = "det-def-sfb-change-of-scalars"
uses = ["def-sfb-modobj-restriction", "def-sfb-modobj-extension", "def-sfb-modobj-extend-restrict-adjunction", "lem-sfb-modobj-extension-right-exact", "lem-sfb-modobj-restriction-preserves-limits", "def-sfb-modobj-coextension", "def-sfb-modobj-restrict-coextend-adjunction", "lem-sfb-modobj-restriction-preserves-colimits", "det-prop-sfb-module-category", "def-sfb-modobj-restriction-equivalence", "def-sfb-modobj-extension-along-iso", "def-sfb-modobj-coextension-along-iso", "def-sfb-modobj-extension-iso-coextension"]
+++
Part 1 is [def-sfb-modobj-restriction].

Part 2: the functor is [def-sfb-modobj-extension] and the adjunction is
[def-sfb-modobj-extend-restrict-adjunction]. So $\operatorname{Ext}_\varphi$ is a left
adjoint and is right exact ([lem-sfb-modobj-extension-right-exact]), and
$\operatorname{Res}_\varphi$ is a right adjoint and preserves limits
([lem-sfb-modobj-restriction-preserves-limits]).

Part 3: the functor is [def-sfb-modobj-coextension] and the adjunction is
[def-sfb-modobj-restrict-coextend-adjunction]. So $\operatorname{Res}_\varphi$ preserves
colimits ([lem-sfb-modobj-restriction-preserves-colimits]).

Part 4 combines parts 2 and 3. In the abelian case $\otimes$ preserves colimits, so
$\mathcal R\otimes-$ and $\mathcal S\otimes-$ are right exact. Then
$\Mod_{\mathcal R}(\mathcal C)$ and $\Mod_{\mathcal S}(\mathcal C)$ are abelian
([det-prop-sfb-module-category]). A functor between abelian categories that preserves
finite limits and finite colimits is exact.

Part 5: the equivalence is [def-sfb-modobj-restriction-equivalence], and the isomorphisms
are [def-sfb-modobj-extension-along-iso], [def-sfb-modobj-coextension-along-iso] and
[def-sfb-modobj-extension-iso-coextension].
