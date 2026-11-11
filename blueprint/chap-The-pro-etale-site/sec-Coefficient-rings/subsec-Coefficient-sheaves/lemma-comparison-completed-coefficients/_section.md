+++
id = "lemma-comparison-completed-coefficients"
kind = "lemma"
title = "Comparison with completed coefficients"
order = 178
lean = ["AlgebraicGeometry.ProEtale.sfb_completed_coefficients"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-site-separably-closed"]
+++
Write $\mathcal O_{E,X}$, $E_X$ and $\QbarX$ for the pullbacks to
$X_{\mathrm{pro}\acute{e}t}$ of $\underline{\mathcal O_E}$, $\underline E$ and
$\underline{\overline{\mathbf Q}_\ell}$. There are canonical isomorphisms of sheaves of rings

$$
\mathcal O_{E,X}\simeq\varprojlim_n(\mathcal O_E/\pi_E^n)_X,
\qquad E_X\simeq\mathcal O_{E,X}[1/\ell],
\qquad \QbarX\simeq\varinjlim_E E_X,
$$

where $(\mathcal O_E/\pi_E^n)_X$ is the constant sheaf. They are
compatible with inverse image along every morphism of schemes.
