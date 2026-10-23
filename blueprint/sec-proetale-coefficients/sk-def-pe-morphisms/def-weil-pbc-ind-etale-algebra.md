+++
id = "def-weil-pbc-ind-etale-algebra"
kind = "definition"
title = "Ind-etale and ind-Zariski algebras"
order = 901
lean = ["Algebra.IndEtale", "RingHom.IndEtale", "Algebra.IndZariski", "Algebra.IsLocalIso", "Algebra.WeaklyEtale", "RingHom.WeaklyEtale", "AlgebraicGeometry.proAffineEtale_Spec_iff", "AlgebraicGeometry.WeaklyEtale.Spec_iff"]
uses = ["def-weil-pbc-scheme-conventions"]
+++
An $A$-algebra is *ind-etale* if it is a filtered colimit of etale algebras
of finite presentation [def-weil-pbc-scheme-conventions]. It is *ind-Zariski*
if it is a filtered colimit of $A$-algebras $C$ that are local isomorphisms:
every prime of $C$ avoids some $g\in C$ such that $A\to C_g$ is a standard
open immersion $A\to A_f$. For instance finite products of localizations
$A_f$ are local isomorphisms. For $A\to B$ ind-etale, the morphism
$\operatorname{Spec}B\to\operatorname{Spec}A$ is an inverse limit of affine
schemes etale over $\operatorname{Spec}A$, and conversely. A ring map
$A\to B$ is *weakly etale* if $B$ is flat over $A$ and the multiplication
$B\otimes_AB\to B$ is flat; equivalently, its map on spectra is weakly etale
in [def-weil-pbc-scheme-conventions].
