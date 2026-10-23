+++
kind = "proof"
of = "lem-weil-pbc-horseshoe-degreewise-map"
+++
A short exact sequence whose first term is injective splits. So in each degree $n$ choose a retraction $r_n:Y^n\to X^n$ of $\alpha_n$ for the source row ($\alpha_nr_n=\mathrm{id}_{X^n}$, diagrammatic order) and a section $s_n:Z'^n\to Y'^n$ of $\beta'_n$ for the target row ($s_n\beta'_n=\mathrm{id}_{Z'^n}$).

Set $t_n=r_n(\varphi_A)_n\alpha'_n+\beta_n(\varphi_C)_ns_n$ ($r$ followed by $\varphi_A$ followed by $\alpha'$, plus $\beta$ followed by $\varphi_C$ followed by $s$). Distributing composition over addition and using the splitting identities and the two zero composites, $\alpha_nt_n=(\varphi_A)_n\alpha'_n+\alpha_n\beta_n(\varphi_C)_ns_n=(\varphi_A)_n\alpha'_n$ and $t_n\beta'_n=r_n(\varphi_A)_n\alpha'_n\beta'_n+\beta_n(\varphi_C)_n=\beta_n(\varphi_C)_n$, which are both outer squares.
