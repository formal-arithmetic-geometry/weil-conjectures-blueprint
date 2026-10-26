+++
id = "det-sp-tower-exceptional-bc"
kind = "lemma"
title = "Exceptional base change for towers and integral coefficients"
order = 3031
uses = ["det-sp-mixed-base-change", "det-sp-tower-gluing", "det-sp-tower-shriek-levels", "det-sp-integral-adjunction-bijection"]
+++
In a Cartesian square as in the sketch, for a finite extension $E/\Ql$:

1. extension by zero and proper base change give a natural isomorphism
   $\beta_{f,\bullet}:v_\bullet^*Rf_{!,\bullet}\xrightarrow{\sim}R(f')_{!,\bullet}u_\bullet^*$ of
   functors $\Dctf(X_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)\to\Dctf(Y'_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$;
2. the transpose of $v_\bullet^*(\varepsilon_{f,\bullet})\circ\beta_{f,\bullet}^{-1}$ under
   the tower adjunction for $f'$ is a natural isomorphism
   $e_{f,\bullet}:u_\bullet^*f_\bullet^!\xrightarrow{\sim}(f')_\bullet^!v_\bullet^*$, whose level $n$
   is the finite exceptional base change $e_{f,\mathcal O_E/\ell^n}$, and which is
   compatible with the reduction maps (hence preserves normalized towers);
3. for $E=\Ql$ and $K\in\Dbc(Y,\Zl)$, $R\varprojlim$ of $e_{f,\bullet}(\operatorname{red}_YK)$ is
   an isomorphism $u_{\Zl}^*f^!_{\Zl}K\xrightarrow{\sim}(f')^!_{\Zl}v^*_{\Zl}K$ in
   $\Dbc(X',\Zl)$, the integral exceptional base change.
