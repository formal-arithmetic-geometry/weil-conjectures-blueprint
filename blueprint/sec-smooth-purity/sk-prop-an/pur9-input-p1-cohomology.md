+++
id = "pur9-input-p1-cohomology"
kind = "remark"
title = "Cohomology of the projective line"
order = 2315
tags = ["latex:bpinput"]
uses = ["pur9-def-projective-line"]
+++
For $Y$ as in Definition [pur9-def-projective-line], the morphism

$$
(\mathcal O_E/\varpi^n)_Y(1)[2]\oplus(\mathcal O_E/\varpi^n)_Y\longrightarrow Rq_{*,\Et,\mathcal O_E/\varpi^n}\bigl((\mathcal O_E/\varpi^n)_{\mathbf P^1_Y}(1)\bigr)[2],
$$

whose first component is the shifted unit and whose second is adjoint to $h$, is an isomorphism in $D^+(Y_{\Et},\mathcal O_E/\varpi^n)$, compatibly with base change in $Y$. *Status:* the older proof combines proper base change (Lemma “The derived proper-base-change comparison” (`pur456-pbc-derived`, see [sk-thm-sf-comp-composition])) with the Kummer computation $H^2(\mathbf P^1,\mu_{\ell^N})=\Pic(\mathbf P^1)/\ell^N$ on geometric fibres; that computation in -prop-h2ZZ is stated over the algebraically closed $k$, whereas geometric fibres of $q$ are over separably closed fields. Imported (detailed blueprint `thm:amb-p1-adjunction`); not proved here.
