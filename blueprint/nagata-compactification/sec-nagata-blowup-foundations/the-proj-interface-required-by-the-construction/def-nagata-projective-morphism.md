+++
id = "def-nagata-projective-morphism"
kind = "definition"
title = "Projective morphism"
order = 179
uses = ["def-nagata-relative-projective-space"]
+++
**Status.** Bypassed by the formalized route: only properness of the global
blow-up is needed, and it is proved directly as
`AlgebraicGeometry.Scheme.IdealSheafData.isProper_blowupMap`; the
global blow-up is never exhibited as a projective morphism.

A morphism $f\colon Y\to X$ is projective if there exist $r\in\mathbb N$
and a closed immersion $Y\hookrightarrow\mathbf P^r_X$ over $X$ whose
composite with the structural morphism is $f$.
