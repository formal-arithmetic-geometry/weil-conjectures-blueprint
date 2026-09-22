+++
id = "lem-fin-finite-reflects-derived"
kind = "lemma"
title = "Finite direct image reflects bounded constructibility"
order = 5164
lean = ["AlgebraicGeometry.Etale.mem_Dbc_of_mem_Dbc_derivedPushforward"]
uses = ["lem-fin-finite-reflects-constructibility"]
+++
Let $p:Z\to S$ be a finite morphism of Noetherian schemes and let $\Lambda$
be a finite commutative ring. On ordinary derived categories of étale
modules, its derived direct image $Rp_*$ reflects membership in $\Dbc$.

## Proof

Exactness of finite direct image gives
$\mathcal H^q(Rp_*K)=p_*\mathcal H^q(K)$. By the finite stalk formula,
$p_*G=0$ forces every $G_{\bar z}=0$, and then $G=0$ by conservativity of
geometric stalks. Thus cohomological bounds on $Rp_*K$ also hold on $K$.
Apply [lem-fin-finite-reflects-constructibility] in each remaining degree to
$G=\mathcal H^q(K)$.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-derived-categories, def:weil-pbc-direct-image, def:weil-pbc-constructible-complexes, lem:weil-pbc-finite-direct-image-exact, lem:weil-pbc-finite-stalk-formula, lem:weil-pbc-geometric-stalk-conservative
