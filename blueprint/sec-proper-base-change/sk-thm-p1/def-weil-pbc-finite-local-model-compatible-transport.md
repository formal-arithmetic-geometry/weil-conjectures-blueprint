+++
id = "def-weil-pbc-finite-local-model-compatible-transport"
kind = "definition"
title = "Natural section-compatible transport"
uses = ["def-pc-scheme", "def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.FiniteLocalModelCompatibleTransport"]
order = 1646
+++
Let $T$ be a scheme [def-pc-scheme], $E$ a sheaf of sets on the small etale site $T_{\Et}$ [def-weil-pbc-etale-site], $U\to T$ an etale $T$-scheme, $Q\to U$ a finite etale $U$-scheme, and $e:E|_U\xrightarrow{\sim}h_Q$ an isomorphism of $E$ restricted to $U_{\Et}$ with the functor of points of $Q$ over $U$. A *compatible transport* for $(E,U,Q,e)$ consists of maps
$$
\mathrm{tr}_{a,b}:\operatorname{Hom}_U((W,a),Q)\longrightarrow\operatorname{Hom}_U((W,b),Q)
$$
for every scheme $W$ and all morphisms $a,b:W\to U$ with the same composite $W\to T$, such that
- **(a)** (naturality) for every $g:W'\to W$ and every $x$ over $a$, $\mathrm{tr}_{ag,bg}(x\circ g)=\mathrm{tr}_{a,b}(x)\circ g$;
- **(b)** (compatibility with $e$) for every etale $T$-scheme $W$, all $T$-morphisms $a,b:W\to U$ and every section $s\in E(W)$, $\mathrm{tr}_{a,b}$ sends the $Q$-point $e(s)$ computed with $W$ viewed over $U$ via $a$ to the $Q$-point $e(s)$ computed via $b$.

No data is chosen and no cocycle condition is imposed.
