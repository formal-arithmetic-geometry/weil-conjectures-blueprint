+++
id = "lemma-unramified-at-infinity-no-linear-characters"
kind = "lemma"
title = "Sheaves unramified at infinity"
order = 1270
lean = ["AlgebraicGeometry.isNonexceptional_of_isUnramifiedAtInfinity"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "lemma-artin-schreier-character-sheaf", "proposition-fourier-transform-middle-extension"]
+++
Let $M$ be an irreducible [lisse](@definition-lisse-sheaves) [Weil sheaf](@definition-weil-structure) on a dense open
$U_0\subset\mathbf A^1_{k_0}$. If $M$ is unramified at infinity and is not geometrically constant,
then no geometric constituent of $M$ is of the form
[$\mathcal L_{\psi(ax)}$](@lemma-artin-schreier-character-sheaf) with $a\in\bar k_0$.
