+++
kind = "proof"
of = "theorem-trace-isomorphism-top-degree--4"
order = 865009
uses = ["theorem-trace-isomorphism-top-degree--2", "proposition-repleteness-pro-etale-topos", "proposition-milnor-sequence"]
+++
Write $\mathcal C_A=\varprojlim_n\mathcal C_{A/U_n}$. Each quotient is finite, and the transition maps are epimorphisms with finite constant kernels $\mathcal C_{U_n/U_{n+1}}$. By [theorem-trace-isomorphism-top-degree--2], both the quotients and these kernels have no cohomology above $2d$. The long exact sequences therefore make the transitions on $H^{2d}$ surjective. Repleteness of the pro-étale topos and the Milnor sequence now give the same upper bound for the limit. Lean packages this last step in `CategoryTheory.Abelian.Ext.subsingleton_of_isLimit_tower`; no finiteness assertion about the cohomology groups is used here.
