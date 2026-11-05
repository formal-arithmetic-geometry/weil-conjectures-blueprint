+++
kind = "proof"
of = "definition-sp-scalar-extension--2"
order = 766003
uses = []
+++
Restriction of scalars is exact. If $U_\varphi$, $U_\psi$ and $U_\chi$
denote its induced functors on the derived categories, then
$U_\varphi\circ U_\psi\simeq U_\chi$, since restriction of scalars along
$\psi\circ\varphi$ is successive restriction along $\psi$ and $\varphi$.
This is `CategoryTheory.Mod.mapDerivedCategoryComapCompIso`.

Derived extension is left adjoint to restriction of scalars
(`CategoryTheory.Mod.derivedExtendMapDerivedCategoryAdjunction`). Composing
the adjunctions for $\varphi$ and $\psi$ and conjugating the preceding
isomorphism gives
$\mathbf L E_\chi\simeq\mathbf L E_\psi\circ\mathbf L E_\varphi$.
The inverse isomorphism evaluated at $K$ gives $(K_B)_C\simeq K_C$.
