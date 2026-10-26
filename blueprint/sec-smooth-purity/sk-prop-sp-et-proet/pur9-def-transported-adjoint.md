+++
id = "pur9-def-transported-adjoint"
kind = "definition"
title = "The transported étale exceptional functor"
order = 2861
uses = ["pur9-def-etale-unbounded-candidate", "sk-prop-sf-comp-coherence", "sk-prop-sf-existence"]
+++
Under Input “An étale right adjoint of the compactification candidate” (`pur9-input-etale-exceptional-adjoint`, in [sk-prop-sf-existence]), for $f$ as in Definition [pur9-def-etale-unbounded-candidate], define

$$
f^{\mathrm{tr}}:=L\nu^*_{X,\mathcal O_E/\pi_E^n}\circ f^{\times}\circ R\nu_{Y,*,\mathcal O_E/\pi_E^n}:D^+(Y_{\Proet},\mathcal O_E/\pi_E^n)\longrightarrow D(X_{\Proet},\mathcal O_E/\pi_E^n),
$$

with Definitions “The derived site direct image” (`pur456-def-site-direct`, in [sk-prop-sf-comp-coherence]) and “The derived site inverse image” (`pur456-def-site-inverse-derived`, in [sk-prop-sf-comp-coherence]). This is the functor called $Rf^!_{\mathcal O_E/\pi_E^n}$ in the source node; it is used here only in the comparison lemma that follows.
