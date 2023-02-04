
namespace International.Airplane.Hangar;

public class Airplane 
{
    private readonly ICrew _crew;
    private IFuel _fuel;
    private readonly Options _options;
    private bool _isOperational;

    public Airplane(ICrew crew, IFuel fuel, Options options, 
        bool isOperational) 
    {
        _crew = crew;
        _fuel = fuel;
        _options = options;
        _isOperational = isOperational;
    }
}