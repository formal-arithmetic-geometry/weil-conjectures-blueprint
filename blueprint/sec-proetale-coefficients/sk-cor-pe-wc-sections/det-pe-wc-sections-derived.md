+++
id = "det-pe-wc-sections-derived"
kind = "lemma"
title = "Free sheaves on weakly contractible objects are projective"
lean = ["AlgebraicGeometry.ProEtale.freeSheafHomEquiv", "AlgebraicGeometry.ProEtale.projective_freeSheaf", "CategoryTheory.Abelian.Ext.eq_zero_of_hasProjectiveDimensionLT"]
order = 930
uses = ["det-pe-weak-contractible-equivalences"]
+++
Let $\Lambda$ be a commutative ring and $U$ an object of $X_{\mathrm{proét}}$. Let
$\Lambda[U]$ be the free sheaf of $\Lambda$-modules on $U$, the sheafification of the presheaf
$V\mapsto\Lambda^{(\Hom_X(V,U))}$. Then $\Hom(\Lambda[U],G)\cong G(U)$, naturally in the sheaf
of $\Lambda$-modules $G$.

If $W$ is a weakly contractible object of $X_{\mathrm{proét}}$
([det-pe-weak-contractible-equivalences]), then $\Lambda[W]$ is a projective object of the
category of sheaves of $\Lambda$-modules on $X_{\mathrm{proét}}$. Consequently
$H^q(W,F)=\operatorname{Ext}^q(\Lambda[W],F)=0$ for every sheaf of $\Lambda$-modules $F$ and
every $q>0$.
