+++
kind = "proof"
of = "lemma-change-coefficients-direct-image--4"
order = 635009
uses = ["corollary-continuity-cohomology", "lemma-inverse-image-coefficient-sheaves"]
+++
Represent $K$ by a bounded below complex $I$ of injective $\mathcal O_{E,X}$-modules. On sheaves, scalar extension is the filtered colimit
$$
E_X\otimes_{\mathcal O_{E,X}}M
\simeq\varinjlim(M\xrightarrow{\ell}M\xrightarrow{\ell}\cdots),
$$
obtained by pulling back the corresponding colimit of condensed coefficient rings. By [corollary-continuity-cohomology], the underived comparison commutes with this colimit, and scalar extension of an injective module is $f_*$-acyclic.

Extension of scalars is exact. Thus $I$ computes $Rf_*K$, and the bounded below complex $E_X\otimes_{\mathcal O_{E,X}}I$ computes $Rf_*(K_E)$. The compatibility of the derived comparison with the underived comparison on $I$, through the units of right derived pushforward and the counits of derived scalar extension, identifies it with an isomorphism.
