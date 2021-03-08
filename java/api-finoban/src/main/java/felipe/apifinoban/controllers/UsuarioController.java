package felipe.apifinoban.controllers;

import felipe.apifinoban.models.Usuario;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Locale;

@RestController
@RequestMapping("/finoban/usuarios")
public class UsuarioController {

    private List<Usuario> listaUsuarios = new ArrayList<Usuario>();

    public UsuarioController() {
        listaUsuarios.add(new Usuario(1, "Jonas",
                "jonas@gmail.com", "123", "01414001",
                "595", new Date()));
        listaUsuarios.add(new Usuario(2, "Travis",
                "travis@gmail.com", "123", "01001000",
                "1", new Date()));
    }

    @PostMapping()
    public String postUsuario(@RequestBody Usuario novoUsuario) {
        listaUsuarios.add(novoUsuario);
        //return "Falha na criação do Usuário";
        return "Usuário criado";
    }

    @GetMapping
    public List<Usuario> getUsuario(@RequestBody String email) {
        List<Usuario> usuarioLogado = new ArrayList<Usuario>();
        for (Usuario u : listaUsuarios) {
            // && u.getSenha().equals(senha)
            if (u.getEmail().equalsIgnoreCase(email)) {
                usuarioLogado.add(u);
                break;
            }
        }
        return usuarioLogado;
    }

    @GetMapping("/todos")
    public List<Usuario> getUsuarios() {
        return listaUsuarios;
    }
}
