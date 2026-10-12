+++
id = "lem-weil-pbc-finite-pullback-identities"
kind = "lemma"
title = "Finite-pullback identities"
order = 1111
lean = ["AlgebraicGeometry.Etale.globalSectionsUpperStarMap_identities"]
uses = ["def-weil-pbc-finite-section-pullback", "def-weil-pbc-inverse-image"]
+++
The pullback of global sections [def-weil-pbc-finite-section-pullback]
satisfies the following four identities, for an etale sheaf $G$ on $T$ and a
commutative square $u\circ a=i\circ b$ with $a:Z'\to T'$, $b:Z'\to Z$,
$u:T'\to T$, $i:Z\to T$:

1. pullback along $\mathrm{id}_T$, followed by $\mathrm{id}_T^{-1}G\cong G$, is
   the identity of $\Gamma(T,G)$;
2. pullback along the composite $u\circ a$, followed by the composition
   isomorphism $(ua)^{-1}G\cong a^{-1}u^{-1}G$, equals $a^\sharp\circ u^\sharp$;
3. pullback commutes with restriction to the closed fibre:
   $\Gamma(\theta)\circ b^\sharp\circ i^\sharp=a^\sharp\circ u^\sharp$, where
   $\theta:b^{-1}i^{-1}G\cong a^{-1}u^{-1}G$ is the square isomorphism;
4. descended sections are preserved: if $x\in\Gamma(T,G)$ and
   $x'\in\Gamma(T',u^{-1}G)$ satisfy $u^\sharp(x)=x'$, then
   $a^\sharp(x')=\Gamma(\theta)(b^\sharp(i^\sharp(x)))$.
