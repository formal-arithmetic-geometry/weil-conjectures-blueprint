+++
kind = "proof"
of = "lemma-inverse-image-tensor-product--3"
order = 494007
uses = ["proposition-extension-zero-restriction-closed-subscheme", "definition-lisse-sheaves"]
+++
The underlying space of $X$ is Noetherian. For a constructible sheaf $M$
on $U$, append the closed complement of $U$ as a zero stratum to a
stratification of $M$. On the original strata, $j_!M$ restricts to $M$;
on the complement it restricts to zero. Hence $j_!M$ is constructible,
as proved by
`AlgebraicGeometry.ProEtale.CondensedRing.isConstructibleModuleObject_openImmersionLowerShriek_obj`.
By [proposition-extension-zero-restriction-closed-subscheme], $j_!$ is exact,
so $H^q(j_!K)\simeq j_!H^q(K)$. It preserves the cohomological bounds and
the constructibility of the cohomology sheaves.
