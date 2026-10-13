+++
id = "pur9-lem-open-restriction-upper-shriek"
kind = "lemma"
title = "Restriction of exceptional images of closed immersions to opens"
order = 2302
tags = ["latex:bplemma"]
uses = ["pur9-input-ambient-composition", "pur9-lem-open-immersion-upper-shriek", "pur9-lem-upper-shriek-composition"]
+++
Assume Input [pur9-input-ambient-composition]. Let $z:Z\hookrightarrow V$ be a closed immersion, $u:U\hookrightarrow Z$ an open immersion, $V_U\subseteq V$ an open subscheme with $z^{-1}(V_U)=U$, $u':V_U\hookrightarrow V$ the inclusion and $z_U:U\hookrightarrow V_U$ the induced closed immersion, so that $zu=u'z_U$. There is a natural isomorphism

$$
r_{z,u}:\mathrm D(u^*_{\mathcal O_E/\varpi^n})Rz^!_{\mathcal O_E/\varpi^n}\xrightarrow{\sim}Rz^!_{U,\mathcal O_E/\varpi^n}\mathrm D(u'^*_{\mathcal O_E/\varpi^n}),
$$

defined as $c_{u',z_U}\circ c_{z,u}^{-1}$ after the identifications $Ru^!_{\mathcal O_E/\varpi^n}=\mathrm D(u^*_{\mathcal O_E/\varpi^n})$, $Ru'^!_{\mathcal O_E/\varpi^n}=\mathrm D(u'^*_{\mathcal O_E/\varpi^n})$ of Lemma [pur9-lem-open-immersion-upper-shriek], with $c$ of Lemma [pur9-lem-upper-shriek-composition].
