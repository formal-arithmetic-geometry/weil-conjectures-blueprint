+++
id = "pur9-def-transported-adjoint"
kind = "definition"
title = "The transported étale exceptional functor"
order = 2146
tags = ["latex:bpdefinition"]
uses = ["pur9-def-etale-unbounded-candidate", "pur9-input-etale-exceptional-adjoint"]
+++
Under Input [pur9-input-etale-exceptional-adjoint], for $f$ as in Definition [pur9-def-etale-unbounded-candidate], define

$$
f^{\mathrm{tr}}:=L\nu^*_{X,\mathcal O_E/\varpi^n}\circ f^{\times}\circ R\nu_{Y,*,\mathcal O_E/\varpi^n}:D^+(Y_{\Proet},\mathcal O_E/\varpi^n)\longrightarrow D(X_{\Proet},\mathcal O_E/\varpi^n),
$$

with Definitions “The derived site direct image” (`pur456-def-site-direct`, see [sk-prop-sf-comp-coherence]) and “The derived site inverse image” (`pur456-def-site-inverse-derived`, see [sk-prop-sf-comp-coherence]). This is the functor called $Rf^!_{\mathcal O_E/\varpi^n}$ in the source node; it is used here only in the comparison lemma that follows.
