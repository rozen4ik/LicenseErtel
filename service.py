from license_server.models import TokenErtel


class Service:
    def get_object_deatil(self, model, id):
        model = model.objects.get(id=id)
        return model

    def create_token(self, request):
        new_token = TokenErtel()
        new_token.token = request.POST.get("token")
        new_token.start_date = request.POST.get("start_date")
        new_token.counterparty = request.POST.get("counterparty")
        new_token.end_date = request.POST.get("end_date")
        new_token.tech_support = request.POST.get("tech_support")
        new_token.number_of_activations = request.POST.get("number_of_activations")
        new_token.notes = request.POST.get("notes")
        new_token.save()
