+++
kind = "proof"
of = "lem-weil-pbc-fpqc-finer-than-etale"
uses = ["def-weil-pbc-etale-site"]
+++
A family $(f_i:U_i\to U)$ of morphisms of the small etale site [def-weil-pbc-etale-site] is a covering family exactly when the underlying morphisms of schemes are jointly surjective onto $U$. Each $f_i$ is a morphism between schemes etale over $T$, hence is itself etale, so flat and locally of finite presentation. Thus $(f_i)$ is an fppf covering of $U$.

Every fppf covering is an fpqc covering: flat morphisms locally of finite presentation are open, so for an affine open $V\subseteq U$ the images $f_i(W)$ of the affine opens $W\subseteq f_i^{-1}(V)$ form an open cover of the quasi-compact space $V$, and finitely many of them suffice (Stacks, Topologies, Lemma 022C). Together with flatness of the $f_i$ this is the fpqc covering condition.
