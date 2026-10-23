+++
kind = "proof"
of = "det-pe-wc-sections-derived"
+++
The natural bijection $\Hom(\Lambda[U],G)\cong G(U)$ is the composite of the sheafification
adjunction, the free–forgetful adjunction between sets and $\Lambda$-modules (applied
objectwise), and the Yoneda lemma.

Let $W$ be weakly contractible, let $e\colon E\to G$ be an epimorphism of sheaves of
$\Lambda$-modules and $f\colon\Lambda[W]\to G$. The epimorphism $e$ is locally surjective, so
its underlying map of sheaves of sets is an epimorphism, and by condition 3 of
[det-pe-weak-contractible-equivalences] the map $E(W)\to G(W)$ is surjective. Under the
bijection above, $f$ corresponds to an element of $G(W)$; a preimage in $E(W)$ corresponds to
a map $g\colon\Lambda[W]\to E$, and $e\circ g=f$ by naturality of the bijection. Hence
$\Lambda[W]$ is projective.

The cohomology $H^q(W,F)$ is $\operatorname{Ext}^q(\Lambda[W],F)$, the derived functors of
$\Hom(\Lambda[W],-)=\Gamma(W,-)$. Since $\Lambda[W]$ is projective, it has projective dimension
$0$, so $\operatorname{Ext}^q(\Lambda[W],F)=0$ for $q>0$.
