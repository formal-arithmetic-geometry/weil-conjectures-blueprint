+++
id = "lemma-acyclic-resolutions"
kind = "lemma"
title = "Acyclic resolutions"
order = 345
lean = ["CategoryTheory.Functor.nonempty_rightDerivedObjIso_homology_of_acyclic", "CategoryTheory.Functor.isIso_rightDerivedFunctorPlusUnit_app_of_rightAcyclic"]
+++
Let $v:\mathcal A\to\mathcal B$ be a left exact additive functor
between abelian categories with enough injectives. If
$F\to M^\bullet$ is a resolution and each $M^m$ is $v$-acyclic, then

$$
\mathcal H^q(vM^\bullet)\simeq R^qvF.
$$

More generally, for a bounded below complex $M^\bullet$ of
$v$-acyclic objects, the canonical comparison
$vM^\bullet\to Rv(M^\bullet)$ is an isomorphism in $D^+(\mathcal B)$.
