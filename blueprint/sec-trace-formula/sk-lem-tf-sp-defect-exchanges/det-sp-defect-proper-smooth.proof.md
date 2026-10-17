+++
kind = "proof"
of = "det-sp-defect-proper-smooth"
uses = ["det-sp-defect-definition", "det-sp-dnc-base-change", "det-sp-nearby-cycles-exchanges", "det-sp-constant-family-vanishing", "thm-weil-pbc-bounded-below"]
+++
By [det-sp-dnc-base-change], $f$ induces $\widetilde f\colon\mathcal D_{Z'}X'\to\mathcal D_ZX$, which
is proper when $f$ is proper and smooth when $f$ is smooth, and $\widetilde f_s^{-1}(Z)=Z'$
schematically, so that $\widetilde f_s\circ e'=e\circ f_Z$ is a cartesian square on special fibres.
Its generic fibre is $f_\eta$, and its restriction to the zero sections is $f_Z\times\mathrm{id}_S$.

*Proper case.* The proper exchange of [det-sp-nearby-cycles-exchanges] for $\widetilde f$ gives
$\operatorname{Sp}_{X,Z}(Rf_*L')\simeq R\widetilde f_{s*}\operatorname{Sp}_{X',Z'}(L')$, and proper
base change [thm-weil-pbc-bounded-below] along the zero section gives
$e^*R\widetilde f_{s*}\simeq Rf_{Z*}e'^*$. On the target side, proper base change gives
$i^*Rf_*L'\simeq Rf_{Z*}i'^*L'$. These identifications carry
$\epsilon_{X,Z}(Rf_*L')$ to $Rf_{Z*}\epsilon_{X',Z'}(L')$: the pullback exchange commutes with
composition, applied to $\widetilde f\circ\widetilde e'=\widetilde e\circ(f_Z\times\mathrm{id}_S)$,
and the specialization units are compatible with the proper exchange by
[det-sp-constant-family-vanishing].

*Smooth case.* The pullback exchange for $\widetilde f$ is invertible, giving
$\widetilde f_s^*\operatorname{Sp}_{X,Z}(L)\simeq\operatorname{Sp}_{X',Z'}(f^*L)$, and
$e'^*\widetilde f_s^*=f_Z^*e^*$, $i'^*f^*=f_Z^*i^*$. Again the composition law for the pullback
exchange and the smooth compatibility of $\sigma$ in [det-sp-constant-family-vanishing] carry
$f_Z^*\epsilon_{X,Z}(L)$ to $\epsilon_{X',Z'}(f^*L)$.

In both cases the squares for $\epsilon$ commute; since $C$ is the cofibre in an enhancement and
$Rf_{Z*}$, $f_Z^*$ are exact, taking cofibres gives the isomorphisms.
