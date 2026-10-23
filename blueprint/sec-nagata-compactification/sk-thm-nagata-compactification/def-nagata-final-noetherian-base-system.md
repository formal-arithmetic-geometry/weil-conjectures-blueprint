+++
id = "def-nagata-final-noetherian-base-system"
kind = "definition"
title = "Noetherian base system used in the final assembly"
lean = ["AlgebraicGeometry.Scheme.noetherianBaseSystem"]
order = 69
uses = ["def-nagata-noetherian-inverse-system", "prop-nagata-noetherian-inverse-system"]
+++
Let $S$ be quasi-compact and quasi-separated. Choose a Noetherian
approximation ([def-nagata-noetherian-inverse-system])

$$
\mathsf N_f=\mathsf N(S)
=(I_S,(S_\lambda)_\lambda,(t_{\mu\lambda})_{\lambda\leq\mu})
$$

of $S$, with limit projections $\pi_\lambda\colon S\to S_\lambda$; one
exists by [prop-nagata-noetherian-inverse-system].
