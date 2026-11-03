+++
id = "lem-weil-pbc-free-yoneda-presheaf-module"
kind = "lemma"
title = "Morphisms out of the free presheaf of modules on a representable are sections"
uses = ["def-weil-presheaf-modules-sheafification"]
lean = ["PresheafOfModules.freeYonedaEquiv", "PresheafOfModules.freeYonedaEquiv_comp", "PresheafOfModules.freeYonedaEquiv_symm_app"]
order = 2068
tags = ["mathlib", "stacks-03EJ"]
+++
Let $\mathcal C$ be a category, $\mathcal O$ a presheaf of rings on $\mathcal C$ and $U$ an object of $\mathcal C$. Let $\mathcal O[h_U ]$ be the presheaf of $\mathcal O$-modules $V\mapsto\bigoplus_{\varphi\in\mathrm{Mor}_{\mathcal C}(V,U)}\mathcal O(V)$ (the free $\mathcal O(V)$-module on the set $\mathrm{Mor}_{\mathcal C}(V,U)$, with basis elements $e_\varphi$), whose restriction along $\psi:V'\to V$ is the $\mathcal O(\psi)$-semilinear map sending $e_\varphi$ to $e_{\varphi\psi}$ (this is the presheaf extension by zero $j_{U!}\mathcal O_U$ of Stacks, sites-modules, Remark 03EJ). Then for every presheaf of $\mathcal O$-modules $\mathcal P$ [def-weil-presheaf-modules-sheafification] the map $\mathrm{Hom}_{\mathrm{PMod}(\mathcal O)}(\mathcal O[h_U ],\mathcal P)\to\mathcal P(U)$, $\beta\mapsto\beta_U(e_{\mathrm{id}_U})$, is a bijection, natural in $\mathcal P$: for $\gamma:\mathcal P\to\mathcal P'$ the element attached to $\gamma\circ\beta$ is $\gamma_U(\beta_U(e_{\mathrm{id}_U}))$. Its inverse sends $s\in\mathcal P(U)$ to the morphism with $e_\varphi\mapsto\mathcal P(\varphi)(s)=s|_\varphi$ on $V$.
