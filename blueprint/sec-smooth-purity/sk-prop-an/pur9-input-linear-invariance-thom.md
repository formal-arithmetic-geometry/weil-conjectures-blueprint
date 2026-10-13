+++
id = "pur9-input-linear-invariance-thom"
kind = "remark"
title = "Linear invariance of the Thom class"
order = 2309
tags = ["latex:bpinput"]
uses = ["pur9-lem-a1-invariance", "pur9-lem-open-immersion-upper-shriek"]
+++
For $g\in\mathrm{GL}_c(\Gamma(B,\mathcal O_B))$, viewed as an automorphism of $\Aaf^c_B$ over $B$ with $gz_c=z_c$, let $a_g$ be the automorphism of $Rz^!_{c,\mathcal O_E/\varpi^n}((\mathcal O_E/\varpi^n)_{\Aaf^c_B}(c))$ obtained from $c_{g,z_c}:Rz^!_{c,\mathcal O_E/\varpi^n}=R(gz_c)^!_{\mathcal O_E/\varpi^n}\to Rz^!_{c,\mathcal O_E/\varpi^n}Rg^!_{\mathcal O_E/\varpi^n}$, $Rg^!_{\mathcal O_E/\varpi^n}=\mathrm D(g^*_{\mathcal O_E/\varpi^n})$ (Lemma [pur9-lem-open-immersion-upper-shriek], $g$ being an isomorphism) and $g^*_{\mathcal O_E/\varpi^n}(\mathcal O_E/\varpi^n)_{\Aaf^c_B}(c)=(\mathcal O_E/\varpi^n)_{\Aaf^c_B}(c)$. Then $a_g[2c]\circ\mathrm{th}_c=\mathrm{th}_c$. *Status:* the older argument decomposes $g$ locally into diagonal, permutation and elementary matrices and uses cup products with supports and Lemma [pur9-lem-a1-invariance]; cup products with supports are not defined in the present framework, so this is imported (detailed blueprint `lem:amb-linear-trace-invariance`), not proved here.
